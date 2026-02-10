import sys
print("Python path:", sys.path)  # يظهر المسارات اللي Python بيدور فيها

# جرب استيراد mediapipe وشوف الـ path الحقيقي
import mediapipe
print("mediapipe module path:", mediapipe.__file__)  # ده هيقولك إيه اللي بيستورد فعليًا

print("Attributes in mediapipe:", [attr for attr in dir(mediapipe) if 'solution' in attr.lower()])  # لازم يظهر 'solutions'

# لو الـ path يشير لملف محلي في مجلدك (مثل D:\DEPI\CV_projects\gaze\mediapipe.py)، ده السبب