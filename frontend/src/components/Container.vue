<template>
  <h3>Contacts</h3>
  <div class="card">
    <div class="card-header">
      Add a new contact
    </div>
    <div class="card-body">
      <div class="row">
        <div class="col">
          <input type="hidden" v-model="id" class form-control mt-2 placeholder="Id">
          <input type="text" v-model="name" class="form-control mt-2" placeholder="Name">
        </div>
        <div class="col">
          <input type="text" v-model="email" class="form-control mt-2" placeholder="Email">
        </div>
        <div class="col">
          <input type="text" v-model="phone" class="form-control mt-2" placeholder="Phone">
        </div>
        <div class="col">
          <button @click="updateOne(this.id)" class="btn btn-block btn-success mt-2">Save</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-header">
        Contact List
      </div>
      <div class="card-body">
        <div class="row">
          <table class="table">
            <thead>
              <th>Id</th>
              <th>Name</th>
              <th>Email</th>
              <th>Phone</th>
              <th>Edit</th>
              <th>Delete</th>
            </thead>
            <tbody>
              <tr v-for="contact in contacts" v-bind:key="contact.id">
                <td>{{contact.id}}</td>
                <td>{{contact.name}}</td>
                <td>{{contact.email}}</td>
                <td>{{contact.phone}}</td>
                <td>
                  <button @click="getOne(contact)" class="btn bn-sm btn-success"><i
                      class="fa-solid fa-pen-to-square"></i></button>
                </td>
                <td>
                  <button @click="deleteOne(contact.id)" class="btn bn-sm btn-success"><i
                      class="fa-solid fa-trash-can"></i></button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Contact-Container',
  props: {
    msg: String
  },
  data(){
    return{
      contacts: null,
      name: '',
      email: '',
      phone: ''
    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/contacts/')
      .then((res)=>{
        this.contacts=res.data
        this.id = ''
        this.name=''
        this.email=''
        this.phone=''
      })
    },
    getOne(contact){
      this.id = contact.id;
      this.name = contact.name;
      this.email = contact.email;
      this.phone = contact.phone;
    },
    deleteOne(id){
      axios.delete(`http://localhost:8000/contacts/${id}/`)
      .then(()=>{
        this.getAll();
      })
    },
    updateOne(id){
      if(id == ''){
        axios.post('http://localhost:8000/contacts/',
        {name:this.name, email:this.email, phone:this.phone})
        .then(()=>{
        this.getAll();
      })
      }else{
        axios.put(`http://localhost:8000/contacts/${id}/`,
        {name:this.name, email:this.email, phone:this.phone})
        .then(()=>{
        this.getAll();
      })
      
      }
    }
  }
}
</script>

<style scoped>

</style>
