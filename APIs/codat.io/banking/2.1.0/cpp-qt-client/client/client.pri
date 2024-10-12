QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccountBalance.h \
    $${PWD}/OAITransaction.h \
    $${PWD}/OAITransactionCategory.h \
# APIs
    $${PWD}/OAIAccountBalancesApi.h \
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAITransactionCategoriesApi.h \
    $${PWD}/OAITransactionsApi.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIAccountBalance.cpp \
    $${PWD}/OAITransaction.cpp \
    $${PWD}/OAITransactionCategory.cpp \
# APIs
    $${PWD}/OAIAccountBalancesApi.cpp \
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAITransactionCategoriesApi.cpp \
    $${PWD}/OAITransactionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
