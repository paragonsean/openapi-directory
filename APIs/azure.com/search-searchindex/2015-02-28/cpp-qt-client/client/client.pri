QT += network

HEADERS += \
# Models
    $${PWD}/OAIDocumentIndexResult.h \
    $${PWD}/OAIIndexActionType.h \
    $${PWD}/OAIIndexingResult.h \
    $${PWD}/OAIQueryType.h \
    $${PWD}/OAISearchMode.h \
    $${PWD}/OAISearchParameters.h \
    $${PWD}/OAISuggestParameters.h \
# APIs
    $${PWD}/OAIDocumentsApi.h \
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
    $${PWD}/OAIDocumentIndexResult.cpp \
    $${PWD}/OAIIndexActionType.cpp \
    $${PWD}/OAIIndexingResult.cpp \
    $${PWD}/OAIQueryType.cpp \
    $${PWD}/OAISearchMode.cpp \
    $${PWD}/OAISearchParameters.cpp \
    $${PWD}/OAISuggestParameters.cpp \
# APIs
    $${PWD}/OAIDocumentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
