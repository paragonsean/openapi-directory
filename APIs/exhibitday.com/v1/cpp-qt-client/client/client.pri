QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIEventsApi.h \
    $${PWD}/OAIFinancialsApi.h \
    $${PWD}/OAIReferencesApi.h \
    $${PWD}/OAISwaggerApi.h \
    $${PWD}/OAITasksApi.h \
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
    $${PWD}/OAIEventsApi.cpp \
    $${PWD}/OAIFinancialsApi.cpp \
    $${PWD}/OAIReferencesApi.cpp \
    $${PWD}/OAISwaggerApi.cpp \
    $${PWD}/OAITasksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
