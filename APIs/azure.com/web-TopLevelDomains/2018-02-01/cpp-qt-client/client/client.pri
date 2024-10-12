QT += network

HEADERS += \
# Models
    $${PWD}/OAITldLegalAgreement.h \
    $${PWD}/OAITldLegalAgreementCollection.h \
    $${PWD}/OAITopLevelDomain.h \
    $${PWD}/OAITopLevelDomainAgreementOption.h \
    $${PWD}/OAITopLevelDomainCollection.h \
    $${PWD}/OAITopLevelDomains_List_default_response.h \
    $${PWD}/OAITopLevelDomains_List_default_response_error.h \
    $${PWD}/OAITopLevelDomains_List_default_response_error_details_inner.h \
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
    $${PWD}/OAITopLevelDomains_List_default_response.cpp \
    $${PWD}/OAITopLevelDomains_List_default_response_error.cpp \
    $${PWD}/OAITopLevelDomains_List_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAITopLevelDomainsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
