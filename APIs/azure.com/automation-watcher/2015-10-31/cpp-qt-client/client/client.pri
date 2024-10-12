QT += network

HEADERS += \
# Models
    $${PWD}/OAIWatcher.h \
    $${PWD}/OAIWatcherListResult.h \
    $${PWD}/OAIWatcherProperties.h \
    $${PWD}/OAIWatcherUpdateParameters.h \
    $${PWD}/OAIWatcherUpdateProperties.h \
    $${PWD}/OAIWatcher_ListByAutomationAccount_default_response.h \
# APIs
    $${PWD}/OAIWatcherApi.h \
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
    $${PWD}/OAIWatcher.cpp \
    $${PWD}/OAIWatcherListResult.cpp \
    $${PWD}/OAIWatcherProperties.cpp \
    $${PWD}/OAIWatcherUpdateParameters.cpp \
    $${PWD}/OAIWatcherUpdateProperties.cpp \
    $${PWD}/OAIWatcher_ListByAutomationAccount_default_response.cpp \
# APIs
    $${PWD}/OAIWatcherApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
