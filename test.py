__author__ = 'woojin'
# -*- coding: utf-8 -*-

para = "Hello World. It's good to see you. Thanks for buying this book."
para_kor = """안녕하세요. 만나서 반갑습니다. 이 책을 구입해 주셔서 감사합니다.
그런데, 이런 문장도 구분할 수 있나요?
음...그렇군요.
테스트입니다."""

from nltk.tokenize import sent_tokenize

print (sent_tokenize(para_kor,'english'))
