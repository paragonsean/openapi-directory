/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISeriestyperule.h
 *
 * 
 */

#ifndef OAISeriestyperule_H
#define OAISeriestyperule_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISeriestyperule : public OAIObject {
public:
    OAISeriestyperule();
    OAISeriestyperule(QString json);
    ~OAISeriestyperule() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint64 getSeriesTypeId() const;
    void setSeriesTypeId(const qint64 &series_type_id);
    bool is_series_type_id_Set() const;
    bool is_series_type_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint64 m_series_type_id;
    bool m_series_type_id_isSet;
    bool m_series_type_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISeriestyperule)

#endif // OAISeriestyperule_H
