/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPodcastsFeatured.h
 *
 * 
 */

#ifndef OAIPodcastsFeatured_H
#define OAIPodcastsFeatured_H

#include <QJsonObject>

#include "OAIPodcast.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPodcast;

class OAIPodcastsFeatured : public OAIObject {
public:
    OAIPodcastsFeatured();
    OAIPodcastsFeatured(QString json);
    ~OAIPodcastsFeatured() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIPodcast> getFeaturedPodcasts() const;
    void setFeaturedPodcasts(const QList<OAIPodcast> &featured_podcasts);
    bool is_featured_podcasts_Set() const;
    bool is_featured_podcasts_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIPodcast> m_featured_podcasts;
    bool m_featured_podcasts_isSet;
    bool m_featured_podcasts_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPodcastsFeatured)

#endif // OAIPodcastsFeatured_H
