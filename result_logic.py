def predict_result(internal_marks, attendance):
    if internal_marks >= 40 and attendance >= 75:
        return "PASS"
    else:
        return "FAIL"
