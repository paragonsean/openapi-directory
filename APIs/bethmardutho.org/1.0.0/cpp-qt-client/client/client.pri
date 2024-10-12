QT += network

HEADERS += \
# Models
    $${PWD}/OAI_lexeme__id__get_200_response.h \
    $${PWD}/OAI_word__id__get_200_response_inner.h \
    $${PWD}/OAI_word__id__get_200_response_inner_word.h \
# APIs
    $${PWD}/OAIAPIApi.h \
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
    $${PWD}/OAI_lexeme__id__get_200_response.cpp \
    $${PWD}/OAI_word__id__get_200_response_inner.cpp \
    $${PWD}/OAI_word__id__get_200_response_inner_word.cpp \
# APIs
    $${PWD}/OAIAPIApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
