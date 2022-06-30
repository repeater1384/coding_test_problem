data = input('현재시각을 입력하세요 : ')

arr = data.split(':')

hour = arr[0]
minute = arr[1]

if minute == '00':
    print('정각입니다.')
else:
    print('정각이 아닙니다.')
