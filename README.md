# paranoid
be aware anytime someone tries to connect to your computer


1: Add the following line to /etc/pam.d/system-auth-ac:
`auth      optional  pam_exec.so /opt/pam_fail.py`

2: Copy the file pam_fail.py to /opt

3: Create /opt/logs with access to all

4: Create a GPG key matching your profile

5: Edit pam_fail.py with your email adress matching your GPG key





