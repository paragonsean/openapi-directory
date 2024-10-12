QT += network

HEADERS += \
# Models
    $${PWD}/OAICO2.h \
    $${PWD}/OAICo2_list_200_response.h \
# APIs
    $${PWD}/OAICo2Api.h \
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
    $${PWD}/OAICO2.cpp \
    $${PWD}/OAICo2_list_200_response.cpp \
# APIs
    $${PWD}/OAICo2Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
