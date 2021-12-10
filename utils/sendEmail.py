# -*- coding: utf-8 -*-
"""
    @File: sendEmail.py
    @Desc: 
    @Time: 2021/12/9 下午10:14
    @Author: Wan Wenlong
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from utils.util import getItemsSection


email_info = getItemsSection('email')


def send_email(attachment):
    msg = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf-8')
    msg['Subject'] = Header(email_info['subject'], 'utf-8')
    msg["Content-Type"] = "application/octet-stream"
    msg["Content-Disposition"] = "attachment;filename=automation_test_report.html"
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = email_info['subject']
    msgRoot.attach(msg)
    try:
        # 连接发送邮件（smtplib模块基本使用格式）
        print('start send test report by email')
        smtp = smtplib.SMTP()
        print('实例化 SMTP success')
        smtp.connect(email_info['smtp_server'])
        print('connect success')
        smtp.login(email_info['sender'], email_info['password'])
        print('login success')
        smtp.sendmail(email_info['sender'], email_info['receivers'], msg.as_string())
        print('send test report success')
        smtp.quit()
    except Exception as e:
        print(f'发送邮件失败{e}')


if __name__ == '__main__':
    # import os
    # import sys
    # print(os.getcwd())
    send_email(r'/Users/wanwl/Documents/work/PythonScript/KDTFrame/reports/2021-12-10_09-35-10.html')
