import http from "./http-common";

class EleveDataService {
  getAll() {
    return http.get("/eleves");
  }

  get(id) {
    return http.get(`/eleves/${id}`);
  }

  create(data) {
    return http.post("/eleves", data);
  }

  update(id, data) {
    return http.put(`/eleves/${id}`, data);
  }

  delete(id) {
    return http.delete(`/eleves/${id}`);
  }

  deleteAll() {
    return http.delete('/eleves');
  }

  findByNom(nom) {
    return http.get(`/eleves/${nom}`);
  }
}

export default new EleveDataService();