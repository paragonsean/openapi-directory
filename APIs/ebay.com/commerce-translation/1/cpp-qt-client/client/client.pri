QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAITranslateRequest.h \
    $${PWD}/OAITranslateResponse.h \
    $${PWD}/OAITranslate_400_response.h \
    $${PWD}/OAITranslation.h \
# APIs
    $${PWD}/OAILanguageApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAITranslateRequest.cpp \
    $${PWD}/OAITranslateResponse.cpp \
    $${PWD}/OAITranslate_400_response.cpp \
    $${PWD}/OAITranslation.cpp \
# APIs
    $${PWD}/OAILanguageApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
