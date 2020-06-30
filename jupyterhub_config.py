# jupyter_config.py

#인증모듈을 LDAP으로 활성화.
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'

#LDAP서버의 주소. 포트와 프로토콜등은 생략하고 작성한다.
c.LDAPAuthenticator.server_address = '192.168.0.230'

#LDAP서버의 포트. Default Port(389)를 사용할 경우 생략가능하다.
c.LDAPAuthenticator.server_port = 30389

#bind_dn_template기능을 활요하기 위해서는 아래를 False로 설정해야한다.
c.LDAPAuthenticator.lookup_dn = False

#LDAP에서 조회할 사용자의 ID의 dn 템플릿 {username}부분이 사용자가 ID로 입력한 값과 치환된다.
c.LDAPAuthenticator.bind_dn_template = [
    "cn={username},cn=kbsys,dc=example,dc=com",
]

#로그인 가능한 사용자 화이트리스트 생성
c.Authenticator.whitelist = {'kbsys', 'yeom'}

#Jupyterhube 로그인시 처음 보여줄 홈 디렉토리
c.Spawner.notebook_dir = '/some/path/to/use'
