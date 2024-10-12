QT += network

HEADERS += \
# Models
    $${PWD}/OAIArticle.h \
    $${PWD}/OAIArticle_multimedia_inner.h \
    $${PWD}/OAIArticle_related_urls_inner.h \
    $${PWD}/OAI_content_json_get_200_response.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIArticle.cpp \
    $${PWD}/OAIArticle_multimedia_inner.cpp \
    $${PWD}/OAIArticle_related_urls_inner.cpp \
    $${PWD}/OAI_content_json_get_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
