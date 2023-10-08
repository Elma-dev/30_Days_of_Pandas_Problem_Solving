import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    stud_sub=students.merge(subjects,how="cross")
    stud_exam_count=examinations.groupby(["student_id","subject_name"]).size().reset_index()
    results=stud_sub.merge(stud_exam_count,how="left").fillna(0).rename(columns={0:"attended_exams"}).sort_values(by=["student_id","student_name","subject_name"])
    return results[["student_id","student_name","subject_name","attended_exams"]]
    
