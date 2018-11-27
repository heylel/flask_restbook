from flask import request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
# 引入web模块
from . import web
__author__ = "gaowenfeng"

@web.route("/book/search/")
def search():
    """
    搜索书籍路由
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            page = form.page.data
            yushu_book.search_by_key(q, page)

        books.fill(yushu_book, q)
    else:
        flash("搜索的关键字不符合要求，请重新输入关键字")

    return render_template("search_result.html", books=books)