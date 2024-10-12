QT += network

HEADERS += \
# Models
    $${PWD}/OAIPost_applicant_single__applicant_multi_request.h \
    $${PWD}/OAIPost_free_end_point__free_request.h \
    $${PWD}/OAIPost_partial_address_multi__partial_address_multi_request.h \
    $${PWD}/OAIPost_postcode_multi__postcode_multi_request.h \
    $${PWD}/OAIPost_proposal_multi__proposal_request.h \
# APIs
    $${PWD}/OAIReversePlanningPermissionAPIApi.h \
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
    $${PWD}/OAIPost_applicant_single__applicant_multi_request.cpp \
    $${PWD}/OAIPost_free_end_point__free_request.cpp \
    $${PWD}/OAIPost_partial_address_multi__partial_address_multi_request.cpp \
    $${PWD}/OAIPost_postcode_multi__postcode_multi_request.cpp \
    $${PWD}/OAIPost_proposal_multi__proposal_request.cpp \
# APIs
    $${PWD}/OAIReversePlanningPermissionAPIApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
