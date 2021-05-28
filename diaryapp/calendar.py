from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Diary

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.user = user
        diary = Diary.objects.filter(user=self.user)
        super(Calendar, self).__init__()

    # 일을 td 태그로 변환하고 이벤트를 일순으로 필터
    def formatday(self, day):
        if day != 0:
            try:
                check = Diary.objects.get(user=self.user, date__year=self.year, date__month=self.month, date__day=day)
                # return f'<td><span class="date">{day}</span><br><img src="/static/checked.png" style="width:100%; height:10px;></td>'
                return f'<td><span class="date" style="font-weight: bold;">{day}</span><br><span>작성완료</span></td>'
            except:
                return '<td><span class="date">{}</span></td>'.format(day)
        return '<td></td>'

    # 주를 tr 태그로 변환
    def formatweek(self, theweek):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d) 
        return f'<tr> {week} </tr>'

    # 월을 테이블 태그로 변환
    def formatmonth(self, withyear=True):
        cal = f'<table class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week)}\n'
        cal += f'</table>'
        return cal