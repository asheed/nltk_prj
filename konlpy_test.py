__author__ = 'woojin'
# -*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()
pprint(kkma.sentences('네, 안녕하세요. 반갑습니다.'))
pprint(kkma.nouns('질문이나 건의사항은 깃허브 이슈 트래커에 남겨주세요.'))
pprint(kkma.pos('오류보고는 실행환경, 에러메시지와 함께 설명을 최대한 상세히!!^^'))
