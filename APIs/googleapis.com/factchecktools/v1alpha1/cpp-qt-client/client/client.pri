QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1Claim.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimRating.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimReview.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponse.h \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1Publisher.h \
# APIs
    $${PWD}/OAIClaimsApi.h \
    $${PWD}/OAIPagesApi.h \
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
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1Claim.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimRating.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimReview.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponse.cpp \
    $${PWD}/OAIGoogleFactcheckingFactchecktoolsV1alpha1Publisher.cpp \
# APIs
    $${PWD}/OAIClaimsApi.cpp \
    $${PWD}/OAIPagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
