QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIPingApi.h \
    $${PWD}/OAIScrapeEmailsApi.h \
    $${PWD}/OAIScrapeStoreLinksApi.h \
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
# APIs
    $${PWD}/OAIPingApi.cpp \
    $${PWD}/OAIScrapeEmailsApi.cpp \
    $${PWD}/OAIScrapeStoreLinksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
