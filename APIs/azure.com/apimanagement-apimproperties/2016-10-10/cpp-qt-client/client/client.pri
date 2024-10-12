QT += network

HEADERS += \
# Models
    $${PWD}/OAIPropertyCollection.h \
    $${PWD}/OAIPropertyContract.h \
    $${PWD}/OAIPropertyCreateParameters.h \
    $${PWD}/OAIPropertyUpdateParameters.h \
    $${PWD}/OAIProperty_Get_default_response.h \
    $${PWD}/OAIProperty_Get_default_response_details_inner.h \
# APIs
    $${PWD}/OAIPropertyApi.h \
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
    $${PWD}/OAIPropertyCollection.cpp \
    $${PWD}/OAIPropertyContract.cpp \
    $${PWD}/OAIPropertyCreateParameters.cpp \
    $${PWD}/OAIPropertyUpdateParameters.cpp \
    $${PWD}/OAIProperty_Get_default_response.cpp \
    $${PWD}/OAIProperty_Get_default_response_details_inner.cpp \
# APIs
    $${PWD}/OAIPropertyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
