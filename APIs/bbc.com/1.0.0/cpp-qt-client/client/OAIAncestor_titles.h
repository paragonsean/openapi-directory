/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAncestor_titles.h
 *
 * 
 */

#ifndef OAIAncestor_titles_H
#define OAIAncestor_titles_H

#include <QJsonObject>

#include "OAIAncestor_titles_brand.h"
#include "OAIAncestor_titles_episode.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAncestor_titles_brand;
class OAIAncestor_titles_episode;

class OAIAncestor_titles : public OAIObject {
public:
    OAIAncestor_titles();
    OAIAncestor_titles(QString json);
    ~OAIAncestor_titles() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAncestor_titles_brand getBrand() const;
    void setBrand(const OAIAncestor_titles_brand &brand);
    bool is_brand_Set() const;
    bool is_brand_Valid() const;

    OAIAncestor_titles_episode getEpisode() const;
    void setEpisode(const OAIAncestor_titles_episode &episode);
    bool is_episode_Set() const;
    bool is_episode_Valid() const;

    QList<OAIAncestor_titles_brand> getSeries() const;
    void setSeries(const QList<OAIAncestor_titles_brand> &series);
    bool is_series_Set() const;
    bool is_series_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAncestor_titles_brand m_brand;
    bool m_brand_isSet;
    bool m_brand_isValid;

    OAIAncestor_titles_episode m_episode;
    bool m_episode_isSet;
    bool m_episode_isValid;

    QList<OAIAncestor_titles_brand> m_series;
    bool m_series_isSet;
    bool m_series_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAncestor_titles)

#endif // OAIAncestor_titles_H
