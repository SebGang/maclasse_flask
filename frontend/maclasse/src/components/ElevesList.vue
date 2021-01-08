<template>
  <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Chercher par nom"
          v-model="nom"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button"
            @click="searchNom(); refreshList()"
          >
            Chercher
          </button>
          <button class="btn btn-outline-secondary" type="button"
            @click="retrieveEleves(); refreshList()"
          >
            Tous les élèves
          </button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <h4>Liste des élèves</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(eleve, index) in eleves"
          :key="index"
          @click="setActiveEleve(eleve, index)"
        >
          {{ eleve.nom.toUpperCase() }} {{ eleve.prenom }}
        </li>
      </ul>
    </div>
    <div class="col-md-6">
      <div v-if="currentEleve">
        <h4>Eleve</h4>
        <div>
          <label><strong>Nom :</strong></label> {{ currentEleve.nom }}
        </div>
        <div>
          <label><strong>Prenom :</strong></label> {{ currentEleve.prenom }}
        </div>
        <div>
          <label><strong>Date de naissance :</strong></label> {{ currentEleve.date_naissance }}
        </div>
        <div>
          <label><strong>Note du premier trimestre :</strong></label> {{ currentEleve.note_trimestre_1 }}
        </div>
        <div>
          <label><strong>Note du premier trimestre :</strong></label> {{ currentEleve.note_trimestre_2 }}
        </div>
        <div>
          <label><strong>Note du deuxième trimestre :</strong></label> {{ currentEleve.note_trimestre_3 }}
        </div>
        <div>
          <label><strong>Moyenne annuelle :</strong></label> {{ moyenneEleve }}
        </div>

        <a class="badge badge-warning"
          :href="'/eleves/' + currentEleve.id"
        >
          Modifier / Supprimer
        </a>
         <button class="badge badge-danger mr-2"
            @click="deleteEleve"
          >
            Supprimer
        </button>
      </div>
      <div v-else>
        <br />
        <p>Cliquer sur un élève...</p>
      </div>
    </div>
  </div>
</template>

<script>
import EleveDataService from "../EleveDataService";
var numeral = require("numeral");

export default {
  name: "eleves-list",
  data() {
    return {
      eleves: [],
      currentEleve: null,
      currentIndex: -1,
      nom: ""
    };
  },
  computed: {
    moyenneEleve: function () {
      return numeral((this.currentEleve.note_trimestre_1 + this.currentEleve.note_trimestre_2 + this.currentEleve.note_trimestre_3) / 3).format("0.0")
    }
  },
  methods: {
    retrieveEleves() {
      EleveDataService.getAll()
        .then(response => {
          this.eleves = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    refreshList() {
      this.currentEleve = null;
      this.currentIndex = -1;
    },

    setActiveEleve(eleve, index) {
      this.currentEleve = eleve;
      this.currentIndex = index;
    },

    deleteEleve() {
      EleveDataService.delete(this.currentEleve.id)
        .then(response => {
          console.log(response.data);
          this.$router.go();
        })
        .catch(e => {
          console.log(e);
        });
    },

    searchNom() {
      EleveDataService.findByNom(this.nom)
        .then(response => {
          this.eleves = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveEleves();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>