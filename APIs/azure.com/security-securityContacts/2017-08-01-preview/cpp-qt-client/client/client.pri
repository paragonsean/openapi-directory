QT += network

HEADERS += \
# Models
    $${PWD}/OAISecurityContact.h \
    $${PWD}/OAISecurityContactList.h \
    $${PWD}/OAISecurityContactProperties.h \
    $${PWD}/OAISecurityContacts_List_default_response.h \
    $${PWD}/OAISecurityContacts_List_default_response_error.h \
# APIs
    $${PWD}/OAISecurityContactsApi.h \
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
    $${PWD}/OAISecurityContact.cpp \
    $${PWD}/OAISecurityContactList.cpp \
    $${PWD}/OAISecurityContactProperties.cpp \
    $${PWD}/OAISecurityContacts_List_default_response.cpp \
    $${PWD}/OAISecurityContacts_List_default_response_error.cpp \
# APIs
    $${PWD}/OAISecurityContactsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
