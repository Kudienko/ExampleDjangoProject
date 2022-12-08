class Index {

    static initPaginator() {
        document.body.querySelectorAll('.pagination > li > a')
                .forEach( link => link.addEventListener('click', Index.pagination_link_clickHandler) );
    }

    static pagination_link_clickHandler(event){
        event.preventDefault(); // запрещаем событие

        let path = event.target.href; // забираем путь
        let page = Global.getURLParameter(path, 'page');

        if (typeof page !== 'undefined') {
            jQuery.ajax({
                url: jQuery(this).attr('action'),
                type: 'POST',
                data: {'page': getURLParameter(path, 'page')}, // забираем номер страницы, которую нужно отобразить

                success : function (json) {
                    // Если запрос прошёл успешно и сайт вернул результат
                    if (json.result)
                    {
                        window.history.pushState({route: path}, "EVILEG", path); // устанавливаем URL в строку браузера
                        jQuery("#articles-list").replaceWith(articles); // Заменяем div со списком статей на новый
                        Index.initPaginator(); // Переинициализируем пагинатор
                        jQuery(window).scrollTop(0); // Скроллим страницу в начало
                    }
                }
            });
        }
    }
}

Index.initPaginator();