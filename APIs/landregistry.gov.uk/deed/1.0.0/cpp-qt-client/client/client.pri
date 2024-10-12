QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdditionalProvisions_inner.h \
    $${PWD}/OAIBorrower.h \
    $${PWD}/OAIChargeClause.h \
    $${PWD}/OAIDeed_Application.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAILender.h \
    $${PWD}/OAIOperative_Deed.h \
    $${PWD}/OAIOperative_Deed_deed.h \
    $${PWD}/OAIPrivateIndividualName.h \
# APIs
    $${PWD}/OAIDeedApi.h \
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAdditionalProvisions_inner.cpp \
    $${PWD}/OAIBorrower.cpp \
    $${PWD}/OAIChargeClause.cpp \
    $${PWD}/OAIDeed_Application.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAILender.cpp \
    $${PWD}/OAIOperative_Deed.cpp \
    $${PWD}/OAIOperative_Deed_deed.cpp \
    $${PWD}/OAIPrivateIndividualName.cpp \
# APIs
    $${PWD}/OAIDeedApi.cpp \
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
