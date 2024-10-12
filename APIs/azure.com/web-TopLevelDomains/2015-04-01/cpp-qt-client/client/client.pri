QT += network

HEADERS += \
# Models
    $${PWD}/OAITldLegalAgreement.h \
    $${PWD}/OAITldLegalAgreementCollection.h \
    $${PWD}/OAITopLevelDomain.h \
    $${PWD}/OAITopLevelDomainAgreementOption.h \
    $${PWD}/OAITopLevelDomainCollection.h \
# APIs
    $${PWD}/OAITopLevelDomainsApi.h \
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
    $${PWD}/OAITldLegalAgreement.cpp \
    $${PWD}/OAITldLegalAgreementCollection.cpp \
    $${PWD}/OAITopLevelDomain.cpp \
    $${PWD}/OAITopLevelDomainAgreementOption.cpp \
    $${PWD}/OAITopLevelDomainCollection.cpp \
# APIs
    $${PWD}/OAITopLevelDomainsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
