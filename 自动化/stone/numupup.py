import xlrd
from xlutils.copy import copy
import os
import xlwt


def ope_excel(xls_name, sheet_name, case_name_col, case_num_col, case_qianzhui, level_num, case_level_name):
    '''
    :param xls_name: 待操作excel名字（仅支持xls格式不支持xlsx格式）
    :param sheet_name:sheet名字
    :param case_name_col:excel里用例名称所在列的列号（自左往右从0开始，如：从0起算A列是0、B列是1...）
    :param case_num_col:excel里用例编号所在列的列号（自左往右从0开始，如：从0起算A列是0、B列是1...）
    :param case_qianzhui:想创建用例编号的前缀（如：mgyy-）
    :param level_num:版本等级列号（自左往右从0开始A列是0、B列是1...）
    :param case_level_name:
    :return:版本等级名
    '''
    # work_book = xlrd.open_workbook('咪咕音乐超编V1.10.0版本测试用例0918.xls')
    work_book = xlrd.open_workbook(xls_name)
    # sheet = work_book.sheet_by_name('es')
    sheet = work_book.sheet_by_name(sheet_name)
    print('sheet_name:{},sheet_rows:{},sheet_cols:{}'.format(sheet.name, sheet.nrows, sheet.ncols))
    rows_num = sheet.nrows  # 获取行号
    # 获取要查询的用例名和用例编号
    search_list1 = []  # 复合用例名、用例编号
    search_list2 = []  # 去空白用例名、用例编号
    case_num_list = []  # 自增用例编号
    for i in range(1, rows_num):
        # search_list1.append((sheet.cell_value(i, 4), sheet.cell_value(i, 5)))  # 用例名列和编号列（从0起算A列是0、B列是1...）
        search_list1.append(
            (sheet.cell_value(i, case_name_col), sheet.cell_value(i, case_num_col)))  # 用例名列和编号列（从0起算A列是0、B列是1...）
    print('all:', search_list1)
    for i in search_list1:
        if i[0] != '':
            search_list2.append(i)
    print('去空用例，用例编号:', search_list2)
    for i in range(1, len(search_list2) + 1):
        # case_num = 'yycb-' + str(i).zfill(3)  # 用例编号前缀
        case_num = case_qianzhui + str(i).zfill(3)  # 用例编号前缀 保存3位有效数字
        case_num_list.append(case_num)
    print('case_num_list:', case_num_list)
    # 将xlrd读取的excel转化成xlwt形式excel；获取第一个sheet
    excel = copy(wb=work_book)
    excel_table = excel.get_sheet(0)
    # print(excel_table)
    j = 0
    for i, value in enumerate(search_list1):
        if value[0] != '':
            excel_table.write(i + 1, case_num_col, case_num_list[j])  # 行号，用例编号列号
            excel_table.write(i + 1, level_num, case_level_name)  # 行号，版本等级列号（从0起算A列是0、B列是1...），版本等级名
            j += 1
    excel.save('yy.xls')  # 另存文件名


if __name__ == '__main__':
    '''
    xls_name:待操作excel名字（仅支持xls格式不支持xlsx格式）
    sheet_name:sheet名字
    case_name_col:excel里用例名称所在列的列号（自左往右从0开始，如：从0起算A列是0、B列是1...）
    case_num_col:excel里用例编号所在列的列号（自左往右从0开始，如：从0起算A列是0、B列是1...）
    case_qianzhui:想创建用例编号的前缀（如：mgyy-）
    level_num:版本等级列号（自左往右从0开始A列是0、B列是1...）
    case_level_name:版本等级名
    '''
    ope_excel('111.xls', 'es', 4, 5, 'mgyy-', 11, 'V3.13.0')
