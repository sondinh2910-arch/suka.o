from datetime import date
from flask import Flask, render_template, request, jsonify
import datetime
import google.generativeai as genai
import webbrowser
import sys

app = Flask(__name__)
API_KEY = "AIzaSyBnixE0qeqmjTUaED83MbCQ1ShgBNF6Zfl"
genai.configure(api_key=API_KEY)


chat_session = None

try:
    model = genai.GenerativeModel("gemini-2.5-flash") 
    chat_session = model.start_chat(history=[])
    print("ok.")
except Exception as e:
    print(f" eror202: {e}") 


def get_bot_response(user_input):
    
    user_input = user_input.lower()
    
    if "hôm nay" in user_input or "ngày" in user_input:
        today = date.today()
        return f"Hôm nay là ngày {today.strftime('%d/%m/%Y')}"
    
    elif "mấy giờ" in user_input or "thời gian" in user_input:
        now = datetime.datetime.now()
        return now.strftime("%H giờ %M phút %S giây")
        
    elif "chào" in user_input or "hello" in user_input:
        return "Chào bạn Sơn đẹp trai, tôi có thể giúp gì cho bạn?"
    
    elif "google" in user_input:
        webbrowser.open("https://google.com")
        return "Đã mở Google trên máy chủ cho bạn."
    
    elif "facebook" in user_input:
        webbrowser.open("https://facebook.com")
        return "Đang mở Facebook trên máy chủ cho bạn."
        
    elif "youtube" in user_input or "mở youtube" in user_input or "youtobe" in user_input:
        webbrowser.open("https://youtube.com")
        return "Đang mở YouTube trên máy chủ cho bạn."
        
    elif "tạm biệt" in user_input or "bye" in user_input:
        return "Tạm biệt bạn Sơn đẹp trai. Hẹn gặp lại!"
        
    else:
        if chat_session is not None:
            try:
                response = chat_session.send_message(user_input) 
                return response.text
            except Exception as e:
                print(f"Lỗi gọi API: {e}")
                return "Xin lỗi, tôi gặp vấn đề khi xử lý yêu cầu này bằng trí tuệ nhân tạo."
        else:
            return "Lỗi: Không thể kết nối với trí tuệ nhân tạo."


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_text = request.form["msg"] 
    bot_reply = get_bot_response(user_text) 
    return jsonify({"answer": bot_reply}) 

#PHẦN 4: KHỞI ĐỘNG SERVER ---
if __name__ == "__main__":
    print("silad____+-*/>>>>>>")
    app.run(debug=True,host='0.0.0.0',port=2910)
