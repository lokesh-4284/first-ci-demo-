def predict_result(marks, attendance):
    """Return PASS only when the student meets both minimum thresholds."""
    if marks >= 70 and attendance >= 75:
        return "PASS"
    return "FAIL"
