QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccount_bidderLocation_inner.h \
    $${PWD}/OAIAccountsList.h \
    $${PWD}/OAICreative.h \
    $${PWD}/OAICreative_corrections_inner.h \
    $${PWD}/OAICreative_disapprovalReasons_inner.h \
    $${PWD}/OAICreative_filteringReasons.h \
    $${PWD}/OAICreative_filteringReasons_reasons_inner.h \
    $${PWD}/OAICreativesList.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAICreativesApi.h \
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
    $${PWD}/OAIAccount_bidderLocation_inner.cpp \
    $${PWD}/OAIAccountsList.cpp \
    $${PWD}/OAICreative.cpp \
    $${PWD}/OAICreative_corrections_inner.cpp \
    $${PWD}/OAICreative_disapprovalReasons_inner.cpp \
    $${PWD}/OAICreative_filteringReasons.cpp \
    $${PWD}/OAICreative_filteringReasons_reasons_inner.cpp \
    $${PWD}/OAICreativesList.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAICreativesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
