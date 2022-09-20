

# menu = {
# 'rus': [{'url': 'projects', 'title': 'Проекты'}, {'url': 'contacts', 'title': 'Контакты'}],
# 'en': [{'url': '.projects', 'title': 'Projects'}, {'url': '.contacts', 'title': 'Contacts'}]
# }

# Navigation panel text
menu = {
'rus': {
'dropmenu':[
{'dropdown_item': {'url': 'services', 'title': 'Услуги'}, 'items': [{'url': 'parsers', 'title': 'Разработка Парсеров'},
                                                                    {'url': 'telegram_bots', 'title': 'Разработка Telegram-ботов'},
                                                                    {'url': 'webapp', 'title': 'Создание веб-приложений'}]}
],
'menu':[
{'url': 'projects', 'title': 'Проекты'},
{'url': 'contacts', 'title': 'Контакты'}
]},

'en': {
'dropmenu':[
{'dropdown_item': {'url': '.services', 'title': 'Services'}, 'items': [{'url': '.parsers', 'title': 'Development parsers'},
                                                                       {'url': '.telegram_bots', 'title': 'Development telegram-bots'},
                                                                       {'url': '.webapp', 'title': 'Create web-application'}]}
],
'menu':[
{'url': '.projects', 'title': 'Projects'},
{'url': '.contacts', 'title': 'Contacts'}
]}}


# Static page's content
content = {
    'rus': {
        'index': """<p class="lead"> В чем мы можем быть полезны для вашего бизнеса: </p>
                
                <ol class="list-group list-group-numbered">
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                      <div class="ms-2 me-auto">
                        <div class="fw-bold">Разработка веб-приложений</div>
                            Разработаем пиложение с административной панелью, мультиязычное, с подключением к базе данных
                        </div>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          <div class="fw-bold">Написание парсеров</div>
                              Программы для сбора и обработки данных с других ресурсов и социальных сетей
                          </div>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          <div class="fw-bold">Написание ботов</div>
                              Разработка Telegram ботов
                          </div>
                    </li>
                </ol>"""
    },


    'en': {
                'index': """<p class="lead"> How can we be useful for your business: </p>
                
                <ol class="list-group list-group-numbered">
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                      <div class="ms-2 me-auto">
                        <div class="fw-bold">Develop web-application</div>
                            We develop applications with an administrative panel, multilingual, with access to the database
                        </div>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          <div class="fw-bold">Parsers</div>
                              Programs for collecting and processing data from other resources and social networks
                          </div>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          <div class="fw-bold">Develop bots</div>
                              Development of Telegram bots
                          </div>
                    </li>
                </ol>"""

    }
}