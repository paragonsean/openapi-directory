QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatasetModel.h \
    $${PWD}/OAIDatasetType.h \
    $${PWD}/OAIDataviewType.h \
    $${PWD}/OAIMonthData.h \
    $${PWD}/OAIMonthModel.h \
    $${PWD}/OAINamespaceData.h \
    $${PWD}/OAINamespaceMetadata.h \
    $${PWD}/OAIPostUsers2FALoginErrorResponse.h \
    $${PWD}/OAIPostUsersLoginErrorResponse.h \
    $${PWD}/OAIPostUsersLoginSuccessResponse.h \
    $${PWD}/OAIResponseData.h \
    $${PWD}/OAIResponseDataFile.h \
    $${PWD}/OAITimespanData.h \
    $${PWD}/OAITimespanModel.h \
    $${PWD}/OAITimespanType.h \
    $${PWD}/OAIUsers2FALoginRequest.h \
    $${PWD}/OAIUsersLoginRequest.h \
    $${PWD}/OAIWeekData.h \
    $${PWD}/OAIWeekModel.h \
    $${PWD}/OAIYearData.h \
    $${PWD}/OAIYearModel.h \
# APIs
    $${PWD}/OAIAuthenticationApi.h \
    $${PWD}/OAIDiscoveryApi.h \
    $${PWD}/OAINamespacesApi.h \
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
    $${PWD}/OAIDatasetModel.cpp \
    $${PWD}/OAIDatasetType.cpp \
    $${PWD}/OAIDataviewType.cpp \
    $${PWD}/OAIMonthData.cpp \
    $${PWD}/OAIMonthModel.cpp \
    $${PWD}/OAINamespaceData.cpp \
    $${PWD}/OAINamespaceMetadata.cpp \
    $${PWD}/OAIPostUsers2FALoginErrorResponse.cpp \
    $${PWD}/OAIPostUsersLoginErrorResponse.cpp \
    $${PWD}/OAIPostUsersLoginSuccessResponse.cpp \
    $${PWD}/OAIResponseData.cpp \
    $${PWD}/OAIResponseDataFile.cpp \
    $${PWD}/OAITimespanData.cpp \
    $${PWD}/OAITimespanModel.cpp \
    $${PWD}/OAITimespanType.cpp \
    $${PWD}/OAIUsers2FALoginRequest.cpp \
    $${PWD}/OAIUsersLoginRequest.cpp \
    $${PWD}/OAIWeekData.cpp \
    $${PWD}/OAIWeekModel.cpp \
    $${PWD}/OAIYearData.cpp \
    $${PWD}/OAIYearModel.cpp \
# APIs
    $${PWD}/OAIAuthenticationApi.cpp \
    $${PWD}/OAIDiscoveryApi.cpp \
    $${PWD}/OAINamespacesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
