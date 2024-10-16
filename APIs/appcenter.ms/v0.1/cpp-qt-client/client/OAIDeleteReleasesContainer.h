/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDeleteReleasesContainer.h
 *
 * 
 */

#ifndef OAIDeleteReleasesContainer_H
#define OAIDeleteReleasesContainer_H

#include <QJsonObject>

#include "OAIDeleteReleasesContainer_releases_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDeleteReleasesContainer_releases_inner;

class OAIDeleteReleasesContainer : public OAIObject {
public:
    OAIDeleteReleasesContainer();
    OAIDeleteReleasesContainer(QString json);
    ~OAIDeleteReleasesContainer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIDeleteReleasesContainer_releases_inner> getReleases() const;
    void setReleases(const QList<OAIDeleteReleasesContainer_releases_inner> &releases);
    bool is_releases_Set() const;
    bool is_releases_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIDeleteReleasesContainer_releases_inner> m_releases;
    bool m_releases_isSet;
    bool m_releases_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeleteReleasesContainer)

#endif // OAIDeleteReleasesContainer_H
