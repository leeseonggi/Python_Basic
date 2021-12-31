for i in range(1,51):
    with open('{0} 주차.txt',format(str(i)),'w',encoding='utf8') as report_file:
        report_file.write('- {0} 주차 주간보고 - '.format(i))
        report_file.write('부서 : ')
        report_file.write('이름 : ')
        report_file.write('업무 요약 : ')

    
