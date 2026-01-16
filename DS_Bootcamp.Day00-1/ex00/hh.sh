#!/bin/sh

if [ $# -eq 1 ]; then
    arg=$1
    encoded_arg=$(echo "$arg" | sed 's/ /%20/g')
    curl -k -H 'User-Agent: api-test-agent' -G "https://api.hh.ru/vacancies?text=$encoded_arg&per_page=20" | jq > hh.json
    echo "Данные записаны успешно"
else
    echo "Отправьте запрос: $0 <название вакансии>"
fi
