from server import DH_Endpoint

message = input("������� �����: ")
a = 194  # �� �������� ��������� ���� ������� ������������ s_public
x = 156 # �� �������� ��������� ���� ������� ������������  s _private
b = 145  # �� �������� ��������� ���� ������� ������������ m_public
y = 112  # �� �������� ��������� ���� ������� ������������ m _private
k1 = 1 # �� ��������
k2 = 1 # �� ��������
user_1 = DH_Endpoint(a, b, x)
user_2 = DH_Endpoint(a, b, y)

u1_partial = user_1.generate_partial_key()  #���������� ���������� ���� ������� ������������ s _partial
# print(u1_partial)

u2_partial = user_2.generate_partial_key()  #���������� ���������� ���� ������� ������������ m _partial
# print(u2_partial)

first_user_full = user_1.generate_full_key(u2_partial)
# print(first_user_full)
m_full = user_2.generate_full_key(u1_partial)
# print(m_full)

msg_encrypted = user_2.encrypt_message(message)
print(msg_encrypted)

message = user_1.decrypt_message(msg_encrypted)
print(message)