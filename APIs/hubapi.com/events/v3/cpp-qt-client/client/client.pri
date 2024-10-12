QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectionResponseExternalUnifiedEvent.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIExternalUnifiedEvent.h \
    $${PWD}/OAINextPage.h \
    $${PWD}/OAIPaging.h \
    $${PWD}/OAIPreviousPage.h \
# APIs
    $${PWD}/OAIEventsApi.h \
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
    $${PWD}/OAICollectionResponseExternalUnifiedEvent.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIExternalUnifiedEvent.cpp \
    $${PWD}/OAINextPage.cpp \
    $${PWD}/OAIPaging.cpp \
    $${PWD}/OAIPreviousPage.cpp \
# APIs
    $${PWD}/OAIEventsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
