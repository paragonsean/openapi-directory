QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthResponse.h \
    $${PWD}/OAIModelError.h \
    $${PWD}/OAIReportsDailyItem.h \
    $${PWD}/OAIReportsDailyResponse.h \
    $${PWD}/OAIReportsWebsiteItem.h \
    $${PWD}/OAIReportsWebsiteResponse.h \
    $${PWD}/OAIReportsWidgetItem.h \
    $${PWD}/OAIReportsWidgetResponse.h \
    $${PWD}/OAITotals.h \
# APIs
    $${PWD}/OAIAuthApi.h \
    $${PWD}/OAIReportsApi.h \
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
    $${PWD}/OAIAuthResponse.cpp \
    $${PWD}/OAIModelError.cpp \
    $${PWD}/OAIReportsDailyItem.cpp \
    $${PWD}/OAIReportsDailyResponse.cpp \
    $${PWD}/OAIReportsWebsiteItem.cpp \
    $${PWD}/OAIReportsWebsiteResponse.cpp \
    $${PWD}/OAIReportsWidgetItem.cpp \
    $${PWD}/OAIReportsWidgetResponse.cpp \
    $${PWD}/OAITotals.cpp \
# APIs
    $${PWD}/OAIAuthApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
