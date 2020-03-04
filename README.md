# Blog-Project-2020

Blog-Project-2020은 사용자가 쉽고 간편하게 콘텐츠를 생성할 수 있는 블로그 플랫폼입니다. [Demo](http://www.for-creator.xyz/)

  - 쉽고 간편한 UI/UX
  - 블로거 전용 대시보드

![for-creator01](https://user-images.githubusercontent.com/51071806/75848256-0d68e300-5e25-11ea-9796-5f8bc7392125.PNG)
![for-creator02](https://user-images.githubusercontent.com/51071806/75848257-0e017980-5e25-11ea-9912-865038672c5f.PNG)
![for-creator03](https://user-images.githubusercontent.com/51071806/75848259-0e017980-5e25-11ea-91ae-e70d01075999.PNG)
![for-creator04](https://user-images.githubusercontent.com/51071806/75848253-0c37b600-5e25-11ea-8d52-7b3e847800e6.PNG)

[Demo](http://www.for-creator.xyz/)


### Tech

Blog-Project-2020은 다양한 오픈 소스를 사용합니다:

* [Django](https://www.djangoproject.com/) - High-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [djangorestframework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs.(REST API)
* [Disqus](https://disqus.com/) - A networked community platform used by hundreds of thousands of sites all over the web.(Comment system)
* [MySQL](https://www.mysql.com/) - The world's most popular open source database
* [TinyMCE](https://www.tiny.cloud/) - The world's most popular JavaScript library for rich text editing
* [tagEditor](https://goodies.pixabay.com/jquery/tag-editor/demo.html) - A powerful and lightweight tag editor plugin for jQuery.
* [Bootstrap](https://getbootstrap.com/) - An open source toolkit for developing with HTML, CSS, and JS.
* [jQuery](https://jquery.com/) - A fast, small, and feature-rich JavaScript library.

### Installation
Blog-Project-2020은 [Python](https://www.python.org/) v3.6+ 환경에서 실행됩니다.

1. 저장소 클론
2. 저장소 위치로 터미널 이동

    ```sh
    $ cd [something path]/blog-project-2020
    ```

3. 가상 환경 패키지 설치

    ```sh
    $ python3 -m venv [directory name]
    ```

4. venv로 환경 설정
    - Linux

        ```sh
        $ source [venv name]/bin/activate
        ```

    - Window

        ```sh
        $ call [venv name]/Scripts/activate
        ```

5. 패키지 환경을 맞춤(설치)

    ```sh
    $ pip install -r requirements.txt
    ```

6. config/setting.py에서 secret_key, Database Access File, AWS Access key 설정이 필요합니다.
