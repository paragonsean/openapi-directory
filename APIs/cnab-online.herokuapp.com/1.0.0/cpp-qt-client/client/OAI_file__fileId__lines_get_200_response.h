/**
 * Cnab Online
 * Processe arquivos de retorno CNAB
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_file__fileId__lines_get_200_response.h
 *
 * 
 */

#ifndef OAI_file__fileId__lines_get_200_response_H
#define OAI_file__fileId__lines_get_200_response_H

#include <QJsonObject>

#include "OAILine.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILine;

class OAI_file__fileId__lines_get_200_response : public OAIObject {
public:
    OAI_file__fileId__lines_get_200_response();
    OAI_file__fileId__lines_get_200_response(QString json);
    ~OAI_file__fileId__lines_get_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAILine> getData() const;
    void setData(const QList<OAILine> &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAILine> m_data;
    bool m_data_isSet;
    bool m_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_file__fileId__lines_get_200_response)

#endif // OAI_file__fileId__lines_get_200_response_H
