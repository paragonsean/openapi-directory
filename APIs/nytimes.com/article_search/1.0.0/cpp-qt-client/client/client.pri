QT += network

HEADERS += \
# Models
    $${PWD}/OAIDoc.h \
    $${PWD}/OAIDoc_byline.h \
    $${PWD}/OAIDoc_headline.h \
    $${PWD}/OAIDoc_keywords.h \
    $${PWD}/OAIDoc_multimedia_inner.h \
    $${PWD}/OAI_articlesearch_json_get_200_response.h \
    $${PWD}/OAI_articlesearch_json_get_200_response_response.h \
    $${PWD}/OAI_articlesearch_json_get_200_response_response_meta.h \
# APIs
    $${PWD}/OAIStoriesApi.h \
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
    $${PWD}/OAIDoc.cpp \
    $${PWD}/OAIDoc_byline.cpp \
    $${PWD}/OAIDoc_headline.cpp \
    $${PWD}/OAIDoc_keywords.cpp \
    $${PWD}/OAIDoc_multimedia_inner.cpp \
    $${PWD}/OAI_articlesearch_json_get_200_response.cpp \
    $${PWD}/OAI_articlesearch_json_get_200_response_response.cpp \
    $${PWD}/OAI_articlesearch_json_get_200_response_response_meta.cpp \
# APIs
    $${PWD}/OAIStoriesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
