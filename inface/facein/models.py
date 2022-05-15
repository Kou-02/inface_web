
from sre_constants import BRANCH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    desig_choice = (
        ('admin','admin'),
        ('staff','staff'),
        ('students','students'),
    )

    department_choice = (
        ('B. Tech. Civil Engineering','B. Tech. Civil Engineering'),
        ('B. Tech. Mechanical Engineering','B. Tech. Mechanical Engineering'),
        ('B. Tech. Automobile Engineering','B. Tech. Automobile Engineering'),
        ('B. Tech. Aeronautical Engineering','B. Tech. Aeronautical Engineering'),
        ('B. Tech. Polymer Engineering','B. Tech. Polymer Engineering'),
        ('B. Tech. Electrical and Electronics Engineering','B. Tech. Electrical and Electronics Engineering'),
        ('B. Tech. Electronics and Communication Engineering','B. Tech. Electronics and Communication Engineering'),
        ('B. Tech. Electronics and Instrumentation Engineering','B. Tech. Electronics and Instrumentation Engineering'),
        ('B. Tech. Artificial Intelligence and Data Science','B. Tech. Artificial Intelligence and Data Science'),
        ('B. Tech. Computer Science and Engineering','B. Tech. Computer Science and Engineering'),
        ('B. Tech. Computer Science and Engineering (Cyber Security)','B. Tech. Computer Science and Engineering (Cyber Security)'),
        ('B. Tech. Computer Science and Engineering (Internet of Things)','B. Tech. Computer Science and Engineering (Internet of Things)'),
        ('B. Tech. Information Technology','B. Tech. Information Technology'),
        ('B. Tech. Biotechnology','B. Tech. Biotechnology'),
        ('B. Tech. Lateral Entry','B. Tech. Lateral Entry'),
        ('B. Arch.','B. Arch.'),
        ('B. Des.','B. Des.'),
        ('B. Pharm.','B. Pharm.'),
        ('BBA LLB (Hons.)','BBA LLB (Hons.)'),
        ('BA LLB (Hons.)','BA LLB (Hons.)'),
        ('B. Sc. Biotechnology','B. Sc. Biotechnology'),
        ('B. Sc. Computer Science','B. Sc. Computer Science'),
        ('BCA','BCA'),
        ('B. Com. General','B. Com. General'),
        ('B. Com. Accounts & Finance','B. Com. Accounts & Finance'),
        ('B. Com. Professional Accounting','B. Com. Professional Accounting'),
        ('B. Com. (Hons.)','B. Com. (Hons.)'),
        ('BBA General','BBA General'),
        ('BBA Financial Services','BBA Financial Services'),
        ('B.A. Public Policy','B.A. Public Policy'),
        ('B.A. English','B.A. English'),
        ('B.A. Islamic Studies','B.A. Islamic Studies'),
        ('M. Tech. Avionics','M. Tech. Avionics'),
        ('M. Tech. Biotechnology','M. Tech. Biotechnology'),
        ('M. Tech. Food Biotechnology','M. Tech. Food Biotechnology'),
        ('M. Tech. CAD-CAM','M. Tech. CAD-CAM'),
        ('M. Tech. Computer Science & Engineering','M. Tech. Computer Science & Engineering'),
        ('M. Tech. Construction Engineering & Project Management','M. Tech. Construction Engineering & Project Management'),
        ('M. Tech. Information Technology','M. Tech. Information Technology'),
        ('M. Tech. Artificial Intelligence and Data Science','M. Tech. Artificial Intelligence and Data Science'),
        ('M. Tech. Structural Engineering','M. Tech. Structural Engineering'),
        ('M. Tech. VLSI & Embedded Systems','M. Tech. VLSI & Embedded Systems'),
        ('M. Tech. Power Systems Engineering','M. Tech. Power Systems Engineering'),
        ('M. Arch.','M. Arch.'),
        ('MBA Business Administration','MBA Business Administration'),
        ('MBA Innovation Entrepreneurship and Venture Development','MBA Innovation Entrepreneurship and Venture Development'),
        ('MCA','MCA'),
        ('LLM (Criminal Law)','LLM (Criminal Law)'),
        ('M. Sc. Actuarial Science','M. Sc. Actuarial Science'),
        ('M. Sc. Chemistry','M. Sc. Chemistry'),
        ('M. Sc. Physics','M. Sc. Physics'),
        ('M. Sc. Biotechnology','M. Sc. Biotechnology'),
        ('M. Sc. Biochemistry & Molecular Biology','M. Sc. Biochemistry & Molecular Biology'),
        ('M. Sc. Microbiology','M. Sc. Microbiology'),
        ('M.Com. (Offered in second shift)','M.Com. (Offered in second shift)'),
        ('M.A. Islamic Studies','M.A. Islamic Studies'),
        ('Ph.D','Ph.D'),
        ('admin','admin'),
        ('others','others'),
         
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    id_no = models.CharField(max_length=70,default='0')
    desig = models.CharField(max_length= 20,choices=desig_choice,default= 'student')
    department = models.CharField(max_length=70,choices=department_choice,default='Ph.D')


    def __str__(self):
        return f'{self.user.username} Profile'