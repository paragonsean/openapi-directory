QT += network

HEADERS += \
# Models
    $${PWD}/OAICountryCode.h \
    $${PWD}/OAICreditDebitIndicator.h \
    $${PWD}/OAICurrencyCode.h \
    $${PWD}/OAIEndBalance.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIFeedConnection.h \
    $${PWD}/OAIFeedConnections.h \
    $${PWD}/OAIPagination.h \
    $${PWD}/OAIStartBalance.h \
    $${PWD}/OAIStatement.h \
    $${PWD}/OAIStatementLine.h \
    $${PWD}/OAIStatements.h \
# APIs
    $${PWD}/OAIBankFeedsApi.h \
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
    $${PWD}/OAICountryCode.cpp \
    $${PWD}/OAICreditDebitIndicator.cpp \
    $${PWD}/OAICurrencyCode.cpp \
    $${PWD}/OAIEndBalance.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIFeedConnection.cpp \
    $${PWD}/OAIFeedConnections.cpp \
    $${PWD}/OAIPagination.cpp \
    $${PWD}/OAIStartBalance.cpp \
    $${PWD}/OAIStatement.cpp \
    $${PWD}/OAIStatementLine.cpp \
    $${PWD}/OAIStatements.cpp \
# APIs
    $${PWD}/OAIBankFeedsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
