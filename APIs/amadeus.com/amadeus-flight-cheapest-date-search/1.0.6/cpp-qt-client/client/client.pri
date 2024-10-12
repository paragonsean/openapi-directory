QT += network

HEADERS += \
# Models
    $${PWD}/OAIDefaults.h \
    $${PWD}/OAIDictionaries.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_404.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIFlightDate.h \
    $${PWD}/OAIFlightDate_links.h \
    $${PWD}/OAIFlightDates.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAILocationValue.h \
    $${PWD}/OAIMeta.h \
    $${PWD}/OAIPrice.h \
# APIs
    $${PWD}/OAIFlightDatesApi.h \
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
    $${PWD}/OAIDefaults.cpp \
    $${PWD}/OAIDictionaries.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_404.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIFlightDate.cpp \
    $${PWD}/OAIFlightDate_links.cpp \
    $${PWD}/OAIFlightDates.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAILocationValue.cpp \
    $${PWD}/OAIMeta.cpp \
    $${PWD}/OAIPrice.cpp \
# APIs
    $${PWD}/OAIFlightDatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
