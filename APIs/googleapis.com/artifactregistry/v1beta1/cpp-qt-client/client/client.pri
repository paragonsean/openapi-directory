QT += network

HEADERS += \
# Models
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIFile.h \
    $${PWD}/OAIHash.h \
    $${PWD}/OAIListFilesResponse.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListPackagesResponse.h \
    $${PWD}/OAIListRepositoriesResponse.h \
    $${PWD}/OAIListTagsResponse.h \
    $${PWD}/OAIListVersionsResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIPackage.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIRepository.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITag.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
    $${PWD}/OAIVersion.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIBinding.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIFile.cpp \
    $${PWD}/OAIHash.cpp \
    $${PWD}/OAIListFilesResponse.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListPackagesResponse.cpp \
    $${PWD}/OAIListRepositoriesResponse.cpp \
    $${PWD}/OAIListTagsResponse.cpp \
    $${PWD}/OAIListVersionsResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIPackage.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIRepository.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITag.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
    $${PWD}/OAIVersion.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
