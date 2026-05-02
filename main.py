def calculate_grade():
    print("--- برنامج نظام التقديرات الذكي ---")
    print("تعليمات: أدخل الدرجة (0-100) للحصول على التقدير، أو اكتب 'خروج' للإنهاء.")

    while True:
        user_input = input("\nالرجاء إدخال درجة الطالب: ").strip().lower()

        # التحقق من رغبة المستخدم في الخروج
        if user_input == "خروج" or user_input == "exit":
            print("يتم الآن إغلاق البرنامج.. شكراً لك!")
            break

        try:
            # محاولة تحويل المدخلات إلى رقم عشري للتعامل مع الكسور
            grade = float(user_input)

            # التحقق من منطقية الدرجة (Handling unexpected values)
            if grade < 0 or grade > 100:
                print("خطأ: الدرجة يجب أن تكون بين 0 و 100 فقط.")
                continue

            # منطق تحديد التقدير
            if grade >= 90:
                result = "ممتاز"
            elif grade >= 80:
                result = "جيد جداً"
            elif grade >= 65:
                result = "جيد"
            else:
                result = "ضعيف"

            print(f"تقدير الطالب هو: ({result})")

        except ValueError:
            # التغلب على المشاكل الناتجة عن إدخال نصوص غير رقمية
            print("خطأ: مدخلات غير صالحة. يرجى إدخال رقم صحيح أو كلمة 'خروج'.")

if __name__ == "__main__":
    calculate_grade()
