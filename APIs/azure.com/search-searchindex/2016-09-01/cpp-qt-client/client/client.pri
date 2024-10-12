QT += network

HEADERS += \
# Models
    $${PWD}/OAIDocumentIndexResult.h \
    $${PWD}/OAIIndexActionType.h \
    $${PWD}/OAIIndexingResult.h \
    $${PWD}/OAIQueryType.h \
    $${PWD}/OAISearchMode.h \
    $${PWD}/OAISearchParametersPayload.h \
    $${PWD}/OAISuggestParametersPayload.h \
# APIs
    $${PWD}/OAIDocumentsProxyApi.h \
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
    $${PWD}/OAISearchParametersPayload.cpp \
    $${PWD}/OAISuggestParametersPayload.cpp \
# APIs
    $${PWD}/OAIDocumentsProxyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
