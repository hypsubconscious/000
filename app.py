from flask import Flask, render_template  # 确保包含 render_template
from flask import request, redirect, url_for  # 你原有的其他导入

app = Flask(__name__)

# 統一的課程數據結構 (同時用於列表和詳情)
courses = [
    {
        'id': 1,
        'name': 'ACHE催眠療癒師課程',
        'image': 'hypnosis.jpg',
        'duration': '10堂課程(實體/線上)',
        'price': 'NT$42,500',
        # 詳情頁專用字段
        'tagline': '美國催眠師協會認證課程',
        'highlights': [
            '國際雙認證資格',
            '包含50個實用催眠技巧',
            '畢業後實習輔導計劃'
        ],
        'details': {
            'outline': ['基礎理論', '技術實操', '案例分析'],
            'target': '適合想轉職療癒工作者',
            'teacher': {
                'name': '林老師',
                'bio': '美國NGH認證催眠導師'
            }
        }
    },
    {
        'id': 2,
        'name': '森林裡的財富療癒課',
        'image': 'forest-healing.jpg',
        'duration': '3小時工作坊',
        'price': 'NT$3,000',
        'tagline': '大自然中的金錢能量調頻',
        'highlights': [
            '戶外自然環境體驗',
            '金錢能量實測練習'
        ],
        'details': {
            'outline': ['金錢信念解析', '能量調頻技巧'],
            'target': '適合想改善財富能量者',
            'teacher': {
                'name': '王老師',
                'bio': '財富能量療癒專家'
            }
        }
    },
    {
        'id': 3,
        'name': '催眠講師培訓課程',
        'image': 'teacher-training.jpg',
        'duration': '6周認證班',
        'price': 'NT$36,000',
        'tagline': '培養專業催眠教學人才',
        'highlights': [
            '教學技巧實戰訓練',
            '課程設計方法論',
            '師資認證考核'
        ],
        'details': {
            'outline': ['教學理論', '教案設計', '實習指導'],
            'target': '適合已有催眠基礎想成為講師者',
            'teacher': {
                'name': '張老師',
                'bio': '資深催眠教育培訓師'
            }
        }
    }
]

# Google 表單連結
course_forms = {
    1: "https://docs.google.com/forms/d/e/1FAIpQLSfKreyCHMJ_gRd7fVO835-Alq2k8oMeeBYlCnKXL9CkTArqVg/viewform?embedded=true",
    2: "https://docs.google.com/forms/d/e/1FAIpQLSc0Wi28xIkCnfP2FaXl5L-4ILpoa_PMreKOw-uFLrkuTsTfsg/viewform?embedded=true",
    3: "https://docs.google.com/forms/d/e/1FAIpQLScZFPSILhhyAfQzfBf0bZ0tLrSMcjJ48PEJcnNskQmgZzGUQg/viewform?embedded=true" 
}

# 新聞數據
news = [
    {'id': 1, 'title': '2023年度最佳教育機構', 'date': '2024-01-15', 'content': '我們榮獲2023年度最佳教育機構獎項...'},
    {'id': 2, 'title': '春季課程優惠活動開始', 'date': '2024-02-01', 'content': '即日起報名春季課程可享早鳥優惠...'}
]

# 路由定義
@app.route('/')
def index():
    return render_template('index.html', courses=courses[:3], news=news[:3])

@app.route('/courses')
def course_list():
    return render_template('courses.html', courses=courses)

@app.route('/courses/<int:course_id>')
def course_detail(course_id):
    course = next((c for c in courses if c['id'] == course_id), None)
    if course:
        return render_template('course_detail.html', course=course)
    return redirect(url_for('course_list'))

@app.route('/select_course', methods=['GET', 'POST'])
def select_course():
    if request.method == 'POST':
        course_id = int(request.form['course'])
        if course_id in course_forms:
            return redirect(url_for('google_form', course_id=course_id))
        return redirect(url_for('course_list'))
    return render_template('select_course.html', courses=courses)

@app.route('/google_form/<int:course_id>')
def google_form(course_id):
    form_url = course_forms.get(course_id)
    if not form_url:
        return redirect(url_for('select_course'))
    return render_template('google_form.html', form_url=form_url)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news_list():
    return render_template('news.html', news=news)

@app.route('/news/<int:news_id>')
def news_detail(news_id):
    news_item = next((item for item in news if item['id'] == news_id), None)
    if news_item:
        return render_template('news_detail.html', news_item=news_item)
    return redirect(url_for('news_list'))



if __name__ == '__main__':
    app.run(debug=True)
